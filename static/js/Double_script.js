const baseUrl = "http://8.137.22.197:5000";

const inputText = document.getElementById('inputText');
const secretKey = document.getElementById('secretKey');
const outputResult = document.getElementById('outputResult');
const DoubleEncryptBtn=document.getElementById('DoubleEncryptBtn');
const DoubleDecryptBtn=document.getElementById('DoubleDecryptBtn');


DoubleEncryptBtn.addEventListener('click', () => {
    const plainText = inputText.value;
    const key = secretKey.value;

    if (!plainText || !key|| key.length !== 32) {
        alert("请输入明文和密钥，同时密钥长度必须为32bit二进制");
        return;
    }

    const requestData = {
        plaintext: plainText,
        secretKey: key
    };

    fetch(`${baseUrl}/aes/encrypt/double`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.code === 0) {
                //outputResult.textContent =data.data.ciphertext;
                //console.log(data);
                outputResult.value=data.data.ciphertext;
            } else {
                alert("加密失败：" + data.msg);
            }
        })
        .catch(error => {
            alert("请求失败：" + error.message);
        });
});

DoubleDecryptBtn.addEventListener('click', () => {
    const cipherText = inputText.value;
    const key = secretKey.value;

    if (!cipherText || !key|| key.length !== 32) {
        alert("请输入密文和密钥，同时密钥长度必须为32bit二进制");
        return;
    }

    const requestData = {
        ciphertext: cipherText,
        secretKey: key
    };

    fetch(`${baseUrl}/aes/decrypt/double`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.code === 0) {
                outputResult.value = data.data.plaintext;
                //console.log(data);
            } else {
                alert("解密失败：" + data.msg);
            }
        })
        .catch(error => {
            alert("请求失败：" + error.message);
        });
});