function notify(type, message, node) {
    options = {
        text: message,
        className: `notification ${type}`,
        close: true,
        duration: -1,
    }
    switch (type) {
        case "info":
            options.style = {
                'background': '#4D8434',
                'color': 'white',
            }
            break;
        case "error":
            options.style = {
                'background': '#CE1B1B',
                'color': 'white',
            }
            break;
    }
    if (!node) {
        options.position = "center"
    } else {
        options.position = "left"
        options.style["flex-direction"] = "row-reverse"
    }
    let toast = Toastify(options)
    toast.showToast();
    $(toast.toastElement).css("transition-property", "top")
    if (node) {
        $(toast.toastElement).css("top", node[0].getBoundingClientRect().top - $(toast.toastElement).height() - 30)
        $(toast.toastElement).css("left", node.offset().left + $(node).width()/2 - $(toast.toastElement).width()/2)
    }
}