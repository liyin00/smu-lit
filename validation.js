

 (function() {
    function constructDataObj(){
        var dataFieldsObj = {

        };
        var fields = document.forms["caseForm"];
        for (i=0; i<fields.length; i++){
            fieldValue = fields[i].value;
            fieldName = fields[i].getAttribute("id");
            dataFieldsObj[fieldName] = fieldValue;
        }
        return dataFieldsObj
    };
    'use strict';
    window.addEventListener('load', function() {
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName('needs-validation');
      // Loop over them and prevent submission
      var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
          }
          else{
            event.preventDefault();
            event.stopPropagation();
            formDataObj = constructDataObj();
            hearingDate = formDataObj.calendarDate;
            clientCaseSummary = formDataObj.caseDescription;
            var settings = {
                "url": "http://localhost:5888/create_case",
                "method": "POST",
                "timeout": 0,
                "headers": {
                  "Content-Type": "application/json"
                },
                "data": JSON.stringify({
                  "s3_url": "s3 url 1",
                  "hearing_date": hearingDate,
                  "case_title": "case title 1",
                  "client_case_summary": clientCaseSummary,
                  "client_id": "1"
                }),
              };
              
              $.ajax(settings).done(function (response) {
                console.log(response);
              });

              window.location.href = "case-success.html";
          }
          form.classList.add('was-validated');
        }, false);
      });
    }, false);
  })();