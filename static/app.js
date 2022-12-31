$(function(){
   function guess_submit() {
      let word = $('#word-input').val();
      $('#played-words').append(`<li>${word}</li>`);
      $('#word-input').val('')
   }
   
   
   $('#word-input').on('submit', (e)=>{
      e.preventDefault();
      guess_submit()
   })

   $('#submit-word').click((e)=>{
      e.preventDefault()
      guess_submit();
   })
   $('form').on('submit', (e)=>{
      e.preventDefault()
      guess_submit();
   })

   async handleWord(e){
      e.preventDefault()
      resp = await axios.get("/handle-word")
   }
})
