document.addEventListener('DOMContentLoaded',(e)=>{

    let subliListContainer=document.querySelectorAll('[data-subtlistDisplayer="list-displayer"]');
    let sublisElement=document.querySelectorAll('[data-sublist="subtitle"]');
    let listArray=  Array.from(sublisElement);
    subliListContainer.forEach((btn,index)=>{
        btn.addEventListener('click',(e)=>{
            e.stopPropagation();
            btn.classList.add('decoration');
            console.log('added..');
            listArray[index].classList.toggle('hidden');
        });

        document.addEventListener('click',(e)=>{
            if(!btn.contains(e.target)){
                btn.classList.remove('decoration');
                listArray[index].classList.add('hidden');
            }
        })
    });
    // We will use this function to update our section base on the clicked button exp: if it's the dashboard button who is clicked our section will re,der infrmation who are related to this sectio  only
    function create_post(){
        let blockContainer=document.querySelector('[data-title="element_container"]');
        let my_div=document.createElement('div');

        //here that is the html code i will update every time 
        let _html=`

                <div class="flex gap-5">
                   <h1 class="text-2xl font-bold text-purple-700">
                
                    Add Post
                  </h1>
                  <div class="flex gap-4">
                    <div class="text-white">
                        <button class="hover:bg-purple-500 p-1 hover:transition-all duration-100 rounded border border-purple-600 transition-all text-purple-500 hover:text-white">Save as Draft</button>
                    </div>
                    <div class="text-white">
                        <button class="bg-purple-500 p-1 rounded hover:translate-y-1 hover:bg-purple-900">Publish</button>
                    </div>
                  </div>
              </div>
        
            <!-- post form creation -->
            <section class=" p-2">
            
                <form action="" method="" class="">
                    
                    
                        <div class="space-y-4 lg:flex gap-10 ">
                            <fieldset class="space-y-3 bg-white rounded-md p-4 basis-2/3">
                                <h3 class="text-xl text-gray-400">Post</h3>
                                <hr>
                                    <p>
                                        <label for="title">Post title</label> <br>
                                        <input type="text" placeholder="Title" class="input-style">
                                    </p>
                                    <p>
                                        <label for="slug">Slug <span class="text-red-600">*</span></label> <br>
                                        <input type="text" placeholder="Type the post Slug field.." class="input-style">
                                    </p>
                                    <p>
                                        <label for="slug">Description <span class="text-red-600">*</span></label> <br>
                                        <input type="text" placeholder="Type the Post descrpiton.." class="input-style">
                                    </p>
                                    <p>
                                        <label for="slug">Reading time <span class="text-red-600">*</span></label> <br>
                                        <input type="text" placeholder="Type the estimate reading time Ex:3 min " class="input-style">
                                    </p>
                                    <p>
                                        <label for="title">Status</label> <br>
                                        <select name="status" id="status">
                                            <option value="none">None</option>
                                            <option value="draf">Publish</option>
                                            <option value="publish">Draft</option>
                                        </select>
                                    </p>
                                    <p>
                                        <label for="title">Category</label> <br>
                                        <select name="category" id="category">
                                            <option value="None">None</option>
                                            <option value="none">Football</option>
                                            <option value="draf">Music</option>
                                            <option value="publish">Art</option>
                                        </select>
                                    </p>
                            </fieldset>
                            <fieldset class="space-y-3  rounded-md  basis-1/2">
                              <div class="bg-white p-4 rounded-md">
                                <h3 class="text-xl text-gray-400">Image</h3>
                                <hr>
                                <img src="../../images/12.jpeg" class="w-20 h-20 m-auto" alt="">
                                <p>
                                    <input type="file">
                                </p>
                              </div>
                              <div class="bg-white p-4 rounded-md">
                                <p>
                                    <label for="publis_date">Publish Date</label>
                                    <input type="date">
                                </p>
                                <p>
                                    <label for="publis_date">Publish time</label>
                                    <input type="time">
                                </p>
                              </div>
                            </fieldset>
                        </div>
                        <div class="mt-4">
                            <label for="content">Text content<span class="text-red-700">*</span></label>
                            <fieldset class="space-y-3 bg-white rounded-md p-6">
                                
                                <textarea name="post_content" id="post_content" class="bg-gray-200 w-[100%] rounded-md" rows="10" placeholder="Your post content goes here.."></textarea>
                            </fieldset>
                        </div>
                        <div class="flex gap-4 mt-4">
                            <div class="text-white">
                                <button class="hover:bg-purple-500 p-1 hover:transition-all duration-100 rounded border border-purple-600 transition-all text-purple-500 hover:text-white">Save as Draft</button>
                            </div>
                            <div class="text-white">
                                <button type="submit" class="bg-purple-500 p-1 rounded hover:translate-y-1 hover:bg-purple-900">Publish</button>
                            </div>
                          </div>
                </form>
            </section>
        
        `;

        my_div.innerHTML=_html;
        blockContainer.innerHTML=my_div.innerHTML;
    }

    function dashboard(){
        let blockContainer=document.querySelector('[data-title="element_container"]');
        let my_div=document.createElement('div');

        //here that is the html code i will update every time 
        let _html=`

            <h1 class="text-2xl font-bold text-purple-700">
        
        Dashboard
      </h1>
      <p>Dashboard/<span class="text-purple-400"> Home</span> </p>

      <!-- Reaction and workflow -->
     <div class="lg:flex justify-between flex-wrap max-md:space-x-4  items-center font-semibold">
      <div class="bg-white p-2 rounded-md ">
        <p class="text-2xl font-bold mb-0">100</p>
        <p class="mt-0">New readers</p>
        <progress value="35" max="100"></progress>
      </div>
      <div class="bg-white p-2 rounded-md ">
        <p class="text-2xl font-bold mb-0">1500</p>
        <p class="mt-0">Trafic</p>
        <progress value="35" max="100"></progress>
      </div>
      <div class="bg-white p-2 rounded-md ">
        <p class="text-2xl font-bold mb-0">90</p>
        <p class="mt-0">New Blog</p>
        <progress value="35" max="100"></progress>
      </div>
      <div class="bg-white p-2 rounded-md ">
        <p class="text-2xl font-bold mb-0">1000</p>
        <p class="mt-0">Likes</p>
        <progress value="35" max="100"></progress>
      </div>
      <div class="bg-white p-2 rounded-md ">
        <p class="text-2xl font-bold mb-0">1500</p>
        <p class="mt-0">Trafic</p>
        <progress value="35" max="100"></progress>
      </div>
      
    </div>

     <!-- content for the followers -->
    <div class="bg-white p-2 rounded-md mt-5 space-y-5 ">
      <h2 class="font-bold text-2xl">New followers </h2>
      <div class="flex justify-between">
        <div class="flex  items-center gap-3">
          <div class="h-10 w-10 "><img class="h-full w-full rounded-full object-cover" src="../../images/3.jpeg" alt=""></div>
            <div class="flex justify-between">
              <div>
                <p class="my-0 text-sm">Franck Detagne</p>
                <p class="my-0 text-gray-400 text-xs">Cameroun</p>
              </div>
            </div>
          </div>
        <button class="block basis-1/12 bg-purple-500 text-white rounded-md text-sm">
          Add
        </button>
      </div>
      <div class="flex justify-between">
        <div class="flex  items-center gap-3">
          <div class="h-10 w-10 "><img class="h-full w-full rounded-full object-cover" src="../../images/3.jpeg" alt=""></div>
            <div class="flex justify-between">
              <div>
                <p class="my-0 text-sm">Franck Detagne</p>
                <p class="my-0 text-gray-400 text-xs">Cameroun</p>
              </div>
            </div>
          </div>
        <button class="block  basis-1/12 bg-purple-500 text-white rounded-md">
          Add
        </button>
      </div>
      <div class="flex justify-between">
        <div class="flex  items-center gap-3">
          <div class="h-10 w-10 "><img class="h-full w-full rounded-full object-cover" src="../../images/3.jpeg" alt=""></div>
            <div class="flex justify-between">
              <div>
                <p class="my-0 text-sm">Franck Detagne</p>
                <p class="my-0 text-gray-400 text-xs">Cameroun</p>
              </div>
            </div>
          </div>
        <button class="block  basis-1/12 bg-purple-500 text-white rounded-md">
          Add
        </button>
      </div>
     
      <div class="flex justify-between">
        <div class="flex  items-center gap-3">
          <div class="h-10 w-10 "><img class="h-full w-full rounded-full object-cover" src="../../images/3.jpeg" alt=""></div>
            <div class="flex justify-between">
              <div>
                <p class="my-0 text-sm">Franck Detagne</p>
                <p class="my-0 text-gray-400 text-xs">Cameroun</p>
              </div>
            </div>
          </div>
        <button class="block  basis-1/12 bg-purple-500 text-white rounded-md">
          Add
        </button>
      </div>
     
    </div>

    <!-- recent action section -->
     <div class="p-2 mt-5 bg-white space-y-4 rounded-md">
      <h1 class="text-2xl font-bold ">Recent Actions</h1>
      <div class="rounded-md bg-white ">
        <div class="lg:flex gap-3 items-center">
          <img src="../../images/fi-rr-arrow-circle-right.svg" alt="" class="w-6 h-6">
          <p>Today</p>
          <img src="../../images/icons8-right-94.png" alt="" class="w-6 h-6">
          <p>You have remove the comment of Mr tech</p>
        </div>
      </div>
      <div class="rounded-md ">
        <div class="lg:flex gap-3 items-center">
          <img src="../../images/fi-rr-arrow-circle-right.svg" alt="" class="w-6 h-6">
          <p>27 MAY</p>
          <img src="../../images/icons8-right-94.png" alt="" class="w-6 h-6">
          <p>You have remove the comment of Mr tech</p>
        </div>
      </div>
      <div class="rounded-md ">
        <div class="lg:flex gap-3 items-center">
          <img src="../../images/fi-rr-arrow-circle-right.svg" alt="" class="w-6 h-6">
          <p>Today</p>
          <img src="../../images/icons8-right-94.png" alt="" class="w-6 h-6">
          <p>You have remove the comment of Mr tech</p>
        </div>
      </div>
      <div class="rounded-md ">
        <div class="lg:flex gap-3 items-center">
          <img src="../../images/fi-rr-arrow-circle-right.svg" alt="" class="w-6 h-6">
          <p>17 June</p>
          <img src="../../images/icons8-right-94.png" alt="" class="w-6 h-6">
          <p>You have remove the comment of Mr tech</p>
        </div>
      </div>
     </div>

     <!-- Marketing channel we will write this section later-->

    <!-- Latest post section -->
    <div class="bg-white rounded-md mt-5 p-2">
      <h1 class="font-bold text-2xl">Latest Posts</h1>
      <ul class="lg:flex flex-wrap items-center">
        <li class=" w-64 max-md:text-xs flex-grow flex-col lg:w-72 mb-5 shadow shadow-[#fdf7f7] p-1 rounded">
          <p class="btn-style">Travel</p>
          <h2 class="text-[1.1rem] font-bold my-1">Set the video play back style with Javascript</h2>
          <div class=" mb-4 lg:w-auto h-52 w-full"><img class="rounded-xl w-full h-full object-cover object-center " src="../../images/11.jpg" alt="banner image 1"></div>
          <div data-title="about-author " >
              <div class="flex gap-1 items-center my-4">
                  <div class="w-5 h-5"><img class="rounded-full" src="../../images/3.jpeg" alt="author profile image"></div>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <h3 class="text-author"><a href="../../html/blog/about_authors.html">Joe Doe</a></h3>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <p class="text-author"> <img src="../../images/fi-rr-calendar.svg" class=" bg-[#ccc] inline w-[12px] h-[12px]" alt=""> 19 August 2024</p>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <p class="text-author"><img src="../../images/face.png" class=" bg-[#ccc] inline w-[12px] h-[12px]" alt=""> 3 min to read</p>
              </div>
              <p class="text-[0.75rem]">Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo ab non 
                  rerum! Vitae dolorum maiores dicta iure quae,   <span class="btn-read-more">Read More <img class="inline-block w-[12px] h-[12px] " src="../../images/arrow-right.png" alt=""></span>
              </p>
          </div>
        </li>
        <li class=" w-64 max-md:text-xs flex-grow flex-col lg:w-72 mb-5 shadow shadow-[#fdf7f7] p-1 rounded">
          <p class="btn-style">Travel</p>
          <h2 class="text-[1.1rem] font-bold my-1">Set the video play back style with Javascript</h2>
          <div class=" mb-4 lg:w-auto h-52 w-full"><img class="rounded-xl w-full h-full object-cover object-center " src="../../images/11.jpg" alt="banner image 1"></div>
          <div data-title="about-author " >
              <div class="flex gap-1 items-center my-4">
                  <div class="w-5 h-5"><img class="rounded-full" src="../../images/3.jpeg" alt="author profile image"></div>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <h3 class="text-author"><a href="../../html/blog/about_authors.html">Joe Doe</a></h3>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <p class="text-author"> <img src="../../images/fi-rr-calendar.svg" class=" bg-[#ccc] inline w-[12px] h-[12px]" alt=""> 19 August 2024</p>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <p class="text-author"><img src="../../images/face.png" class=" bg-[#ccc] inline w-[12px] h-[12px]" alt=""> 3 min to read</p>
              </div>
              <p class="text-[0.75rem]">Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo ab non 
                  rerum! Vitae dolorum maiores dicta iure quae,   <span class="btn-read-more">Read More <img class="inline-block w-[12px] h-[12px] " src="../../images/arrow-right.png" alt=""></span>
              </p>
          </div>
        </li>
        <li class=" w-64 max-md:text-xs flex-grow flex-col lg:w-72 mb-5 shadow shadow-[#fdf7f7] p-1 rounded">
          <p class="btn-style">Travel</p>
          <h2 class="text-[1.1rem] font-bold my-1">Set the video play back style with Javascript</h2>
          <div class=" mb-4 lg:w-auto h-52 w-full"><img class="rounded-xl w-full h-full object-cover object-center " src="../../images/11.jpg" alt="banner image 1"></div>
          <div data-title="about-author " >
              <div class="flex gap-1 items-center my-4">
                  <div class="w-5 h-5"><img class="rounded-full" src="../../images/3.jpeg" alt="author profile image"></div>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <h3 class="text-author"><a href="../../html/blog/about_authors.html">Joe Doe</a></h3>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <p class="text-author"> <img src="../../images/fi-rr-calendar.svg" class=" bg-[#ccc] inline w-[12px] h-[12px]" alt=""> 19 August 2024</p>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <p class="text-author"><img src="../../images/face.png" class=" bg-[#ccc] inline w-[12px] h-[12px]" alt=""> 3 min to read</p>
              </div>
              <p class="text-[0.75rem]">Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo ab non 
                  rerum! Vitae dolorum maiores dicta iure quae,   <span class="btn-read-more">Read More <img class="inline-block w-[12px] h-[12px] " src="../../images/arrow-right.png" alt=""></span>
              </p>
          </div>
        </li>
        <li class=" w-64 max-md:text-xs flex-grow flex-col lg:w-72 mb-5 shadow shadow-[#fdf7f7] p-1 rounded">
          <p class="btn-style">Travel</p>
          <h2 class="text-[1.1rem] font-bold my-1">Set the video play back style with Javascript</h2>
          <div class=" mb-4 lg:w-auto h-52 w-full"><img class="rounded-xl w-full h-full object-cover object-center " src="../../images/11.jpg" alt="banner image 1"></div>
          <div data-title="about-author " >
              <div class="flex gap-1 items-center my-4">
                  <div class="w-5 h-5"><img class="rounded-full" src="../../images/3.jpeg" alt="author profile image"></div>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <h3 class="text-author"><a href="../../html/blog/about_authors.html">Joe Doe</a></h3>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <p class="text-author"> <img src="../../images/fi-rr-calendar.svg" class=" bg-[#ccc] inline w-[12px] h-[12px]" alt=""> 19 August 2024</p>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <p class="text-author"><img src="../../images/face.png" class=" bg-[#ccc] inline w-[12px] h-[12px]" alt=""> 3 min to read</p>
              </div>
              <p class="text-[0.75rem]">Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo ab non 
                  rerum! Vitae dolorum maiores dicta iure quae,   <span class="btn-read-more">Read More <img class="inline-block w-[12px] h-[12px] " src="../../images/arrow-right.png" alt=""></span>
              </p>
          </div>
        </li>
        <li class=" w-64 max-md:text-xs flex-grow flex-col lg:w-72 mb-5 shadow shadow-[#fdf7f7] p-1 rounded">
          <p class="btn-style">Travel</p>
          <h2 class="text-[1.1rem] font-bold my-1">Set the video play back style with Javascript</h2>
          <div class=" mb-4 lg:w-auto h-52 w-full"><img class="rounded-xl w-full h-full object-cover object-center " src="../../images/11.jpg" alt="banner image 1"></div>
          <div data-title="about-author " >
              <div class="flex gap-1 items-center my-4">
                  <div class="w-5 h-5"><img class="rounded-full" src="../../images/3.jpeg" alt="author profile image"></div>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <h3 class="text-author"><a href="../../html/blog/about_authors.html">Joe Doe</a></h3>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <p class="text-author"> <img src="../../images/fi-rr-calendar.svg" class=" bg-[#ccc] inline w-[12px] h-[12px]" alt=""> 19 August 2024</p>
                  <span class="inline-block w-px h-3 bg-slate-500"></span>
                  <p class="text-author"><img src="../../images/face.png" class=" bg-[#ccc] inline w-[12px] h-[12px]" alt=""> 3 min to read</p>
              </div>
              <p class="text-[0.75rem]">Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo ab non 
                  rerum! Vitae dolorum maiores dicta iure quae,   <span class="btn-read-more">Read More <img class="inline-block w-[12px] h-[12px] " src="../../images/arrow-right.png" alt=""></span>
              </p>
          </div>
        </li>
      </ul>
    </div>
        
        
        `

        my_div.innerHTML=_html;
        blockContainer.innerHTML=my_div.innerHTML;
    }
    let displayer= ()=> {
        document.addEventListener('click',(e)=>{
            let btns=document.querySelectorAll('button');
            btns.forEach((btn,index) => {
                if(btn.contains(e.target)&&btn.id==="post_btn_id"){
                    create_post();
                    btn.classList.toggle('decoration');
                }
                else if(btn.contains(e.target)&&btn.id==="dashboard_btn_id"){
                    dashboard();
                    btn.classList.toggle('decoration');
                }
            });
            
        })
    };

    //call function section
    displayer();
    
});