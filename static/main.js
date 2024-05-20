function showAlert() {
    alert("Valor registrado com sucesso!");
}

document.addEventListener("DOMContentLoaded", function() {
    const metodoSelect = document.getElementById('metodo');
    const conteudoDiv = document.querySelector('.conteudo');
    
    
    const conteudo = `<select name="parcelas" id="parcelas" required>
    <option value="" selected disabled hidden>Número de parcelas</option>
    <option value="1x">1x</option>
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