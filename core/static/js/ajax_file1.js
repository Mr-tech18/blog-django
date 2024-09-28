document.addEventListener('DOMContentLoaded',()=>{

    (
        
        ()=>{
         
            document.getElementById('btnSubmit1').addEventListener('click', function (e) {
                e.preventDefault();
                
                // Retrieve the form
                let myForm = document.getElementById('myForm');
                let formData = new FormData(myForm); // FormData contains all the form fields, including the CSRF token
                
                // Create the XHR object
                let xhr = new XMLHttpRequest();
                
                // Open the communication
                xhr.open("POST", myForm.getAttribute('action'), true);
                
                // Set the CSRF token in the header if not already present
                xhr.setRequestHeader('X-CSRFToken', formData.get('csrfmiddlewaretoken'));
                
                xhr.onreadystatechange = function () {
                    if (this.readyState == 3) {
                        console.log('Loading the request...');
                        
                    }

                    if (this.readyState == 4 && this.status == 200) {
                        
                        let data=JSON.parse(this.responseText);
                        let comment_container=document.getElementById('comment_block');
                        let btnContainer=document.getElementById('btn_btn_comment');
                        //let firstChildr=btnContainer.firstElementChild;
                        let text=null;
                        if (data.context.comments_count>1){
                            text=document.createTextNode(`( ${data.context.comments_count} )`)
                        }
                        else{
                            text=document.createTextNode(`( ${data.context.comments_count} )`)
                        }
                        let span=document.createElement('span');
                        
                        span.appendChild(text);
                        span.setAttribute('class',"font-bold");
                        btnContainer.replaceChild(span,btnContainer.firstElementChild);
                       
                        //displaying the comment section dynamically

                        let date=new Date();
                        
                        let _html = ''; // Initialize as an empty string
                        _html += '<div class="max-lg:text-xs border shadow rounded-xl mb-3 p-1 ">';
                        _html += '<div class="flex items-center gap-3">';
                        _html += '<div class="h-12 ">';
                        _html += '<img class=" rounded-full h-full w-full object-cover" src="{{request.user.profile_image.url}}">';
                        _html += '</div>';
                        _html += '<div class="">';
                        _html += '<div class="flex gap-4">';
                        _html += '<p class="font-bold">' + data.context.user + '</p>';
                        _html += '<p>' + date.getMinutes() + ' ago </p>';
                        _html += '</div>';
                        _html += '</div>';
                        _html += '</div>';
                        _html += '<div class="relative ml-14">';
                        _html += '<!--content of the comment-->';
                        _html += '<div class="">' + data.context.content + '</div>';
                        _html += '<div class="mt-2">';
                        _html += '<button class="bg-gray-300 rounded-xl p-1 w-20 hover:bg-gray-300">Like 12</button>';
                        _html += '<button class="bg-gray-300 rounded-xl p-1 w-20 hover:bg-gray-300">Dislike 1</button>';
                        _html += '<button class="bg-gray-300 rounded-xl p-1 w-20 hover:bg-gray-300">reply 30</button>';
                        _html += '</div>';
                        _html += '</div>';
                        _html += '</div>';
                        
                        // Create a temporary container to insert the HTML as an element
                        let tempDiv = document.createElement('div');
                        tempDiv.innerHTML = _html;
                        
                        // Prepend the new element to the container
                        document.getElementById('comment_container').insertBefore(tempDiv.firstChild,myForm.nextElementSibling);
                        
                        myForm.reset();

                        console.log('The request was successful');
                    } 
                    
                    xhr.onerror=function(){
                        console.log('an error occur...');
                    }
                };
                
                // Send the form data directly without converting to JSON
                xhr.send(formData);
            });
            
        }
    )();
})