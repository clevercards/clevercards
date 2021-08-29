const modalBtn = document.getElementById('myModalBtn');
const modalBody = document.getElementById('modal-body-confirm');
const startBtn = document.getElementById('start-button');

const url = window.location.href;

modalBtn.addEventListener('click', () => {
    const pk = document.querySelector('input[name="sample-post"]:checked').getAttribute('data-pk');
    const subjectName = document.querySelector('input[name="sample-post"]:checked').value;
    const numQuestions = document.querySelector('input[name="sample-num"]:checked').value;
    localStorage.setItem('subjectName', subjectName);
    localStorage.setItem('numQuestions', numQuestions);
    let time;
    if (numQuestions == 3) {
        time = 1;
    } else if (numQuestions == 5) {
        time = 2;
    } else if (numQuestions == 10) {
        time = 3;
    }
    modalBody.innerHTML = `
        <div class="h5 mb-3">Are you ready to begin "<b>${subjectName}</b>" ?</div>
        <div class="text-muted">
            <ul>
                <li>Subject: <b>${subjectName}</b></li>
                <li>Number of questions: <b>${numQuestions}</b></li>
                <li>Time: <b>${time} minutes.</b></li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click', ()=>{
        window.location.href = url + pk;
    })
})
