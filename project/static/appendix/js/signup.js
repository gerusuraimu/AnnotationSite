const password = document.getElementById('password')


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
    });
}


window.onload = function() {
    setCrypto();
};
