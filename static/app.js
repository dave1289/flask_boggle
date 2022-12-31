$(function(){
   let time = 60
   // setInterval(()=>{
   //    time -= 1;
   //    $('#timer').val() = time
   // }, 1000)
   function guess_submit() {
      let word = $('#word-input').val();
      $('#played-words').append(`<li>${word}</li>`);
      $('#word-input').val('')
   }

   $('#word-input').on('submit', (e)=>{
      e.preventDefault();
      guess_submit()
   })

   $('#submit-word').click(guess_submit)
})

