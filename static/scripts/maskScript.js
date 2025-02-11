document.addEventListener('DOMContentLoaded', function() {
    var phoneInputs = document.querySelectorAll('.phone-mask');

    phoneInputs.forEach(function(phoneInput) {
      // Initialize intlTelInput
      const iti = intlTelInput(phoneInput, {
        separateDialCode: true,
        initialCountry: "auto", // Automatically select the country based on the user's location
        geoIpLookup: function(callback) {
            $.get("https://ipinfo.io", function() {}, "jsonp").always(function(resp) {
              var countryCode = (resp && resp.country) ? resp.country : "us";
              callback(countryCode);
            });
        },
        utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.13/js/utils.js" // Include utils.js for formatting and validation
      });

      // Function to update the phone number value (including the dial code)
      function updatePhoneNumber() {
        const fullNumber = iti.getNumber(); // Get the full number with dial code
        phoneInput.value = fullNumber;       // Update the input field value
      }

      // Listen for changes to the number
      phoneInput.addEventListener('countrychange', updatePhoneNumber); // Use "countrychange" event
      phoneInput.addEventListener('keyup', updatePhoneNumber);

      // Store the initial number (if any)
      updatePhoneNumber();
    });
  });