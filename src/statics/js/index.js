setTimeout(() => {
    let span = document.createElement('span');
    document.body.appendChild(span);

    setInterval(() => {
        span.innerHTML = Date();
    }, 10);
}, 10);