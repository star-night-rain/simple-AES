const baseUrl = "http://8.137.22.197:5000";

const inputText1 = document.getElementById('inputText1');
const inputText2 = document.getElementById('inputText2');
const CrackBtn=document.getElementById('CrackBtn');
const outputResult = document.getElementById('outputResult');
const timeResult = document.getElementById('Time');

CrackBtn.addEventListener('click', () => {
    const plaintexts = inputText1.value.split(',').map(pt => pt.trim()).filter(pt => pt !== '');
    const ciphertexts = inputText2.value.split(',').map(ct => ct.trim()).filter(ct => ct !== '');

    if (plaintexts.length === 0 || ciphertexts.length === 0 || plaintexts.length !== ciphertexts.length) {
        alert("请输入明文和密文，并确保它们数量相同且不为空");
        return;
    }

    const requestData = {
        plaintexts: plaintexts,
        ciphertexts: ciphertexts
    };

    fetch(`${baseUrl}/aes/crack`, {
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
                console.log(data);
                if(data.data.count>=1){
                    outputResult.value = data.data.secret_keys.join(', ');
                    timeResult.value = data.data.duration;
                }else{
                    alert("明文/密文对的密钥不相同");
                }

            } else {
                alert("破解失败：" + data.msg);
            }
        })
        .catch(error => {
            alert("请求失败：" + error.message);
        });
});