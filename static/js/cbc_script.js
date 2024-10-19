const baseUrl = "http://8.137.22.197:5000";

const inputText = document.getElementById('inputText');
const secretKey = document.getElementById('secretKey');
const initialVector=document.getElementById('initialVector');
const outputResult = document.getElementById('outputResult');
const cbcEncryptBtn=document.getElementById('cbcEncryptBtn');
const cbcDecryptBtn=document.getElementById('cbcDecryptBtn');

cbcEncryptBtn.addEventListener('click', () => {
    const plainText = inputText.value;
    const key = secretKey.value;
    const iv=initialVector.value;

    if (!plainText || !key|| key.length !== 16) {
        alert("请输入明文和密钥，同时密钥长度必须为16bit二进制");
        return;
    }
    if ( !iv||iv.length !== 16) {
        alert("请输入初始向量，同时初始向量必须为16bit二进制");
        return;
    }

    const requestData = {
        plaintext: plainText,
        secretKey: key,
        initialVector:iv
    };

    fetch(`${baseUrl}/aes/cbc/encrypt`, {
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
                //console.log(data);
            } else {
                alert("加密失败：" + data.msg);
            }
        })
        .catch(error => {
            alert("请求失败：" + error.message);
        });
});

cbcDecryptBtn.addEventListener('click', () => {
    const cipherText = inputText.value;
    const key = secretKey.value;
    const iv=initialVector.value;
    if (!cipherText || !key|| key.length !== 16) {
        alert("请输入密文和密钥，同时密钥长度必须为16bit二进制");
        return;
    }
    if ( !iv|| iv.length !== 16) {
        alert("请输入初始向量，同时初始向量必须为16bit二进制");
        return;
    }
    const requestData = {
        ciphertext: cipherText,
        secretKey: key,
        initialVector:iv
    };

    fetch(`${baseUrl}/aes/cbc/decrypt`, {
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
                console.log(data);
            } else {
                alert("解密失败：" + data.msg);
            }
        })
        .catch(error => {
            alert("请求失败：" + error.message);
        });
});