const salesForm = document.querySelector('#sales-form');
const salesResult = document.querySelector('#sales-result');

salesForm.addEventListener('submit', (event) => {
  event.preventDefault();
  let firstInvalid = null;
  for (const field of salesForm.querySelectorAll('input, textarea')) {
    field.value = field.value.trim();
    let message = '';
    if (!field.value) {
      message = 'Completa este campo.';
    } else if (field.name === 'email' && !field.validity.valid) {
      message = 'Ingresa un correo válido.';
    } else if (field.name === 'phone' && !field.validity.valid) {
      message = 'Ingresa entre 7 y 15 dígitos, sin espacios ni símbolos.';
    } else if (field.name === 'ponds' && !field.validity.valid) {
      message = 'Ingresa una cantidad entera mayor que cero.';
    } else if (!field.validity.valid) {
      message = 'Revisa el valor de este campo.';
    }
    document.querySelector(`#error-${field.name}`).textContent = message;
    field.setAttribute('aria-invalid', String(Boolean(message)));
    if (message && !firstInvalid) firstInvalid = field;
  }
  if (firstInvalid) {
    salesResult.textContent = 'Revisa los campos indicados.';
    firstInvalid.focus();
    return;
  }
  salesResult.textContent = 'Datos válidos. Esta es una demostración: no se ha enviado ni guardado una solicitud.';
});
salesForm.addEventListener('input', () => {
  salesResult.textContent = '';
});
