window.addEventListener('load', function(){

    const elements = document.querySelectorAll('select[multiple]');
    elements.forEach((element, key, parent) => {
        const placeholder = element.dataset.placeholder;
        const choices = new Choices(element, {
            removeItemButton: true,
            placeholderValue: placeholder,
        });
    })

})
