







function filter_positive () {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.set('patient_status', 'Tested Positive');

      window.location.search = urlParams;
  }
  function filter_quarantined () {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.set('patient_status', 'Quarntined');

      window.location.search = urlParams;
  }
  function filter_dead () {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.set('patient_status', 'Dead');

      window.location.search = urlParams;
  }
  function filter_any_status () {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.delete('patient_status');

      window.location.search = urlParams;
  }
  function filter_age_1 () {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.set('age__lt', '18');
      urlParams.set('age__gte', '0');
      window.location.search = urlParams;
  }
  function filter_age_2 () {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.set('age__lt', '30');
      urlParams.set('age__gte', '18');


      window.location.search = urlParams;
  }
  function filter_age_3 () {
    const urlParams = new URLSearchParams(window.location.search);
      
      urlParams.set('age__lt', '60');
      urlParams.set('age__gte', '30');



      window.location.search = urlParams;
  }
  function filter_age_3 () {
    const urlParams = new URLSearchParams(window.location.search);
      urlParams.lt('age_lt','200')
      urlParams.set('age__gte', '60');
      



      window.location.search = urlParams;
  }
  function filter_age_any () {
    const urlParams = new URLSearchParams(window.location.search);
      urlParams.delete('age_lt');
      urlParams.delete('age__gte');
      



      window.location.search = urlParams;
  }






  function filter_treatment_any() {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.delete('treatment');

      window.location.search = urlParams;
  }  
  function filter_treatment_1 () {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.set('treatment', 'Home');

      window.location.search = urlParams;
  }  
  function filter_treatment_2 () {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.set('treatment', 'Workplace');

      window.location.search = urlParams;
  }  
  function filter_treatment_3() {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.set('treatment', 'Hospital');

      window.location.search = urlParams;
  }

  function filter_test_any() {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.delete('tests');

      window.location.search = urlParams;
  }  function filter_test_1() {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.set('tests', 'PCR');

      window.location.search = urlParams;
  }
  function filter_test_2() {
    const urlParams = new URLSearchParams(window.location.search);

      urlParams.set('tests', 'Antigen');

      window.location.search = urlParams;
  }