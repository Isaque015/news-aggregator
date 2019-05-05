u("form").handle('submit', async e => {
    body = {
        nickname: u("#nickname").first().value,
        password: u("#password").first().value
    }

    const response = await fetch('/sign_in', {
        headers: {
            'Content-Type': 'application/json'
        },
        method: 'POST',
        body: JSON.stringify(body)
    }).then(res => res.json())  ;

    if (response.code == 200) {
        window.location.href = '/';
    }
    toastr.error(response.msg)
});
