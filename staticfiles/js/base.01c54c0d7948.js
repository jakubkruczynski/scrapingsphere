const questionInputs = document.querySelectorAll('.question-input');
let checkedInputs = [];

questionInputs.forEach((input) => {
  input.addEventListener('click', () => {
    if (input.checked) {
      if (checkedInputs.length === 2) {
        const oldestInput = checkedInputs.shift();
        oldestInput.checked = false;
      }
      checkedInputs.push(input);
    } else {
      const index = checkedInputs.indexOf(input);
      checkedInputs.splice(index, 1);
    }
    questionInputs.forEach((otherInput) => {
      if (otherInput !== input) {
        otherInput.checked = false;
      }
    });
  });
});
