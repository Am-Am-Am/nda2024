// Скрипт, создающий маску для номеров в формах

$(document).ready(function() {
    // Функция для инициализации масок на всех полях с классом .phone-mask
    function initializePhoneMasks() {
        $('.phone-mask').each(function() {
            var phoneInput = this;

            if (!$(this).hasClass('initialized')) {
                // Initialize intlTelInput
                const iti = intlTelInput(phoneInput, {
                    separateDialCode: true,
                    initialCountry: "ru", // Russia by default
                    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.13/js/utils.js", // Include utils.js for formatting and validation
                    autoPlaceholder: "aggressive", // Enable the autoPlaceholder option
                    nationalMode: true,      // Display only national numbers
                });


                // Mark as initialized
                $(this).addClass('initialized');
            }
        });
    }

    // Инициализация масок при первой загрузке страницы
    initializePhoneMasks();

    // Обработчик для отслеживания появления новых полей с классом .phone-mask
    $(document).on('focus', '.phone-mask', function() {
        var phoneInput = this;

        if (!$(this).hasClass('initialized')) {
            initializePhoneMasks();
        }
    });

    // Инициализация масок при открытии модального окна
    $('#modal').on('shown.bs.modal', function () {
        initializePhoneMasks();
    });
});