console.log('Hello Quiz')
const url = window.location.href;

const quizBox = document.getElementById('quiz-box')
let data 

$.ajax({
    type: 'GET',
        url: `${url}data`,
        success: function(response){
            // console.log(response)
            data = response.data
            data.forEach(el => {
                for (const [question, ansers] of Object.entries(el)){
                    console.log(question)
                    console.log(ansers)
                }
            })

        },
        error: function(error){
            console.log(error)
        }
})