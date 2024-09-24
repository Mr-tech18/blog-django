document.addEventListener('DOMContentLoaded',()=>{

    (
        
        ()=>{
         
            document.getElementById('btnSubmit1').addEventListener('click',function(e){
                e.preventDefault();
                //let's retrieve the form and convert it into a json object
                let myForm=document.getElementById('myForm');
                console.log("the form itself: "+myForm)
                let formData=new FormData(myForm);
                console.log("the formData itself: "+formData)

                let jsonForm=JSON.stringify(Object.fromEntries(formData.entries()));
                console.log(jsonForm);
                //xhr object declaration
                let xhr=new XMLHttpRequest();
                //here we open the communication between the browser and the server
                xhr.open("POST",myForm.getAttribute('action'),true);
                
                //now we set the header of the request
                xhr.setRequestHeader('X-CSRFToken', '{{ csrf_token }}');


                xhr.onreadystatechange=function(){
                    if(this.readyState==3){
                        console.log('loading the request...');
                    }
                    if(this.readyState==4 && this.status==200){
                        console.log('the request is sucessfull satisfy');
                    }
                    else{
                        console.log('an error accure during the the processing of your request...');
                    }
                }

              

                

                xhr.send(jsonForm);
            });
        }
    )();
})