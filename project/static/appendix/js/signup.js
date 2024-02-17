const password = document.getElementById('password')
const confirm = document.getElementById('confirm')


async function hashText(text) {
    const encoder = new TextEncoder();
    const data = encoder.encode(text);
    const hashBuffer = await crypto.subtle.digest('SHA-512', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}


function setCrypto() {
    password.addEventListener('change', async function() {
        password.value = await hashText(password.value);
        if (0 < password.value.length) {
            confirm.disabled = false;
        } else {
            confirm.disabled = true;
        }
    });
}


window.onload = function() {
    confirm.disabled = true;
    setCrypto();
};
