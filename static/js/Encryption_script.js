const baseUrl = "http://8.137.22.197:5000";

const inputText = document.getElementById('inputText');
const secretKey = document.getElementById('secretKey');
const outputResult = document.getElementById('outputResult');
const BitEncryptBtn=document.getElementById('BitEncryptBtn');
const StringEncryptBtn=document.getElementById('StringEncryptBtn');

BitEncryptBtn.addEventListener('click', () => {
    const plainText = inputText.value;
    const key = secretKey.value;

    if (!plainText || !key|| key.length !== 16) {
        alert("请输入明文和密钥，同时密钥长度必须为16bit二进制");
        return;
    }

    const requestData = {
        plaintext: plainText,
        secretKey: key
    };

    fetch(`${baseUrl}/aes/encrypt/single/bit`, {
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
                outputResult.value = data.data.ciphertext;
            } else {
                alert("加密失败：" + data.msg);
            }
        })
        .catch(error => {
            alert("请求失败：" + error.message);
        });
});

StringEncryptBtn.addEventListener('click', () => {
    const plainText = inputText.value;
    const key = secretKey.value;

    if (!plainText || !key|| key.length !== 16) {
        alert("请输入明文和密钥，同时密钥长度必须为16bit二进制");
        return;
    }

    const requestData = {
        plaintext: plainText,
        secretKey: key
    };

    fetch(`${baseUrl}/aes/encrypt/single/string`, {
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
                outputResult.value = data.data.ciphertext;
            } else {
                alert("加密失败：" + data.msg);
            }
        })
        .catch(error => {
            alert("请求失败：" + error.message);
        });
});