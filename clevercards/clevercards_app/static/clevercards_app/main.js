const modalBtns = [...document.getElementsByClassName('modal-button')];
const modalBody = document.getElementById('modal-body-confirm');
const startBtn = document.getElementById('start-button');

const url = window.location.href;

modalBtns.forEach(modalBtn => {
    modalBtn.addEventListener('click', () => {
        const pk = modalBtn.getAttribute('data-pk');
        const name = modalBtn.getAttribute('data-quiz');
        const numQuestions = modalBtn.getAttribute('data-questions');
        const time = modalBtn.getAttribute('data-time');
    
        modalBody.innerHTML = `
            <div class="h5 mb-3">Are you ready to begin "<b>${name}</b>" ?</div>
            <div class="text-muted">
                <ul>
                    <li>Quiz: <b>${name}</b></li>
                    <li>number of questions: <b>${numQuestions}</b></li>
                    <li>time: <b>${time} minutes.</b></li>
                </ul>
            </div>
        `

        startBtn.addEventListener('click', ()=>{
            window.location.href = url + pk;
        })
    })
});
