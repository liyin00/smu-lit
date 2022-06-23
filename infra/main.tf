resource "aws_s3_bucket" "client-media-bucket" {
  bucket = "client-media-bucket"

  tags = {
    Name        = "client-media-bucket"
  }
}

resource "aws_s3_bucket" "client-media-log-bucket" {
  bucket = "client-media-log-bucket"

  tags = {
    Name        = "client-media-log-bucket"
  }
}

resource "aws_s3_bucket_versioning" "client-media-bucket-versioning" {
  bucket = aws_s3_bucket.client-media-bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_acl" "client-media-bucket-acl" {
  bucket = aws_s3_bucket.client-media-bucket.id
  acl    = "log-delivery-write"
}

resource "aws_s3_bucket_logging" "client-media-logging" {
  bucket = aws_s3_bucket.client-media-bucket.id

  target_bucket = aws_s3_bucket.client-media-log-bucket.id
  target_prefix = "log/"
}

# to prevent credentials leak on db, injection of variables are performed. Copy and paste from .env file 
resource "aws_db_instance" "penteract" {
  allocated_storage    = 20
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t3.micro"
  db_name              = "penteract"
  username             = var.db_username
  password             = var.db_password
  parameter_group_name = "default.mysql5.7"
  skip_final_snapshot  = true
  multi_az             = "yes"
  backup_window        = "00:00-01:00"
}

# iam configuration for cicd pipeline 
data "aws_iam_policy_document" "ec2-read-s3-policy-doc" {
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["codedeploy.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "pipeline-role" {
  name                  = "pipeline-role"
  assume_role_policy    = data.aws_iam_policy_document.ec2-read-s3-policy-doc.json
  force_detach_policies = true

  tags = merge(var.common_tags, {
    Name = "pipeline-role"
  })
}

resource "aws_iam_role_policy_attachment" "pipeline-policy" {
  role       = aws_iam_role.config_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSCodeDeployRole"
}