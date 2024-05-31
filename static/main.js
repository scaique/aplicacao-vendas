// Visualização das parcelas
document.addEventListener("DOMContentLoaded", function() {
    const metodoSelect = document.getElementById('metodo');
    const conteudoDiv = document.querySelector('.conteudo');
    
    
    const conteudo = `<select name="parcelas" id="parcelas" required>
    <option value="1x" selected>1x</option>
    <option value="2x">2x</option>
    <option value="3x">3x</option>
    <option value="4x">4x</option>
    <option value="5x">5x</option>
    <option value="6x">6x</option>
</select>
<br>`;

    metodoSelect.addEventListener('change', function() {
        if (this.value === 'Credito') {
            conteudoDiv.innerHTML = conteudo;
        } else {
            conteudoDiv.innerHTML = '';
        }
    });
});

// Validação do formulário
document.getElementById('numeros').addEventListener('input', function(e) {
    this.setCustomValidity('');
    const input = e.target;
    const pattern = /^[0-9 ]*$/;
    if (pattern.test(input.value)) {
        input.classList.remove('invalido');
        input.classList.add('valido');
        document.getElementById('aviso').setAttribute('hidden', '')
    }
    if (!pattern.test(input.value)) {
        input.classList.remove('valido');
        input.classList.add('invalido');
        document.getElementById('aviso').removeAttribute('hidden')
    }
    if (input.value === "") {
        input.classList.remove('invalido');
        input.classList.remove('valido');
        document.getElementById('aviso').setAttribute('hidden', '')
    }
});

// Notificação
document.addEventListener('DOMContentLoaded', function() {
    var notification = document.getElementById('notification');
    if (notification) {
        setTimeout(function() {
            notification.style.display = 'none';
        }, 15000);
    }
});

// Contador de tempo
function countTimer(tempo, display) {
    setInterval(() => {
        display.textContent = `(${tempo--}s)`;
        if (tempo < 0) tempo = 0;
    }, 1000);
}

window.onload = () => countTimer(14, document.querySelector('#timer'));