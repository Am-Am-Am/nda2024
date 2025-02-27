// Скрипт, создающий маску для номеров в формах


  let utilsScriptLoaded = false;

  async function loadUtilsScript(url) {
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = url;
      script.onload = () => {
        utilsScriptLoaded = true;
        resolve();
      };
      script.onerror = reject;
      document.head.appendChild(script);
    });
  }

  $(document).ready(async function() {
    try {
      await loadUtilsScript("../../../static/scripts/utils.min.js");
    } catch (error) {
      console.error("Ошибка загрузки utilsScript:", error);
      return;
    }

    function initializePhoneMasks() {
      $('.phone-mask:not([data-intl-tel-input-initialized])').each(function() {
        const phoneInput = this;

        const iti = intlTelInput(phoneInput, {
          separateDialCode: true,
          initialCountry: "ru",
          autoPlaceholder: "aggressive",
          nationalMode: true,
        });

        $(this).attr('data-intl-tel-input-initialized', 'true');
      });
    }

    initializePhoneMasks();

    $('#modal').on('shown.bs.modal', function() {
      initializePhoneMasks();
    });

    $(document).off('focus', '.phone-mask'); // Удаляем лишний обработчик
  });
