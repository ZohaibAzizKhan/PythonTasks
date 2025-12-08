const posts=[];

const headingInput=document.getElementById('heading-input');
const messageInput=document.getElementById('message');
const postButton=document.getElementById('post-button');
// when user clicks on post article nav hide home article and show post article form
const postArticle=document.getElementById('post-article-nav');
// when user clicks on home article nav hide post article form and show home article
const homeArticle=document.getElementById('home-article-nav');

// user profile article display
const userProfileNav=document.getElementById('user-profile-nav');
userProfileNav.addEventListener('click',function(){
  document.getElementById('user-profile-article').classList.remove('hidden');
  document.getElementById('display-posts').classList.add('hidden');
  document.getElementById('post-article-form').classList.add('hidden');
})
postArticle.addEventListener('click',function(){
    const hidePostForm=document.getElementById('post-article-form');
    hidePostForm.classList.add('hidden');
    document.getElementById('user-profile-article').classList.add('hidden')
    document.getElementById('display-posts').classList.remove('hidden');
});
homeArticle.addEventListener('click',function(){
    document.getElementById('post-article-form').classList.remove('hidden');
    document.getElementById('user-profile-article').classList.add('hidden');
    document.getElementById('display-posts').classList.add('hidden');
});
// headerProfile nav
const headerProfileNav=document.getElementById('header-profile-nav');
headerProfileNav.addEventListener('click',function(){
  document.getElementById('user-profile-article').classList.remove('hidden');
  document.getElementById('display-posts').classList.add('hidden');
  document.getElementById('post-article-form').classList.add('hidden');
})
console.log(headingInput.value)

// exatract heading and message on button click
postButton.addEventListener('click',function(){
  console.log('Post button clicked');
    const heading=headingInput?.value.trim();
    const message=messageInput?.value.trim();
    if(!heading || !message){
        alert('Please enter both heading and message');
        return;
    }
    const post={
      id:posts.length+1,
      heading:heading,
      message:message,
      timestamp:new Date().toDateString(),
      hastags:document.getElementById('hashTags').value.trim().split(',').filter(tag=>tag.startsWith('#'))
    }
        console.log(`Heading: ${post.heading}, Message: ${post.message}`);
        const postElement=document.createElement('div');
        postElement.className='post w-auto flex flex-col p-4 border border-gray-300 bg-gray-200 rounded gap-10 mb-4 shadow-md relative';
        postElement.innerHTML=`
            <div class="flex justify-between"> 
            <h2 class="text-2xl font-bold mb-2">${post.heading}</h2>
            <svg class="
            post-dropdown text-black font-bold cursor-pointer w-[31px] h-[31px] " aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-width="2.4" d="M12 6h.01M12 12h.01M12 18h.01"/>
</svg>
 <div class="dropdown-menu absolute right-0 top-10 bg-white border rounded shadow-md w-36 hidden z-10">
      <ul>
        <li class="px-4 py-2 hover:bg-green-200 cursor-pointer">Share</li>
        <li class="px-4 py-2 hover:bg-green-200 cursor-pointer">Like</li>
        <li class="px-4 py-2 hover:bg-green-200 cursor-pointer">Comment</li>
      </ul>
    </div>
  </div>

        <p class="text-gray-700">${post.message}</p>
        <p class='text-sm text-gray-500'>Posted on: ${new Date().toLocaleString()}</p>
        <p class="text-sm text-gray-500">${post.hastags.join(', ')}</p>
        <div class="flex w-1/6 justify-between items-center mt-4">
        <svg class="like-icon w-[31px] cursor-pointer h-[31px] text-gray-700 hover:text-red-500" id="like-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4" d="M12.01 6.001C6.5 1 1 8 5.782 13.001L12.011 20l6.23-7C23 8 17.5 1 12.01 6.002Z"/>
  </svg> 

<svg class="dislike-icon w-[31px] h-[31px]  text-blue-400
hover:text-blue-500 cursor-pointer" id="dislike-icon" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4" d="M9 17h6l3 3v-3h2V9h-2M4 4h11v8H9l-3 3v-3H4V4Z"/>
</svg>
<svg class="delete-icon w-[31px] h-[31px] hover:text-red-500 cursor-pointer text-red-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.4" d="M5 7h14m-9 3v8m4-8v8M10 3h4a1 1 0 0 1 1 1v3H9V4a1 1 0 0 1 1-1ZM6 7h12v13a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V7Z"/>
</svg>

        </div>


        `;
        document.getElementById('display-posts').appendChild(postElement);

});
// for displaying posts
const postsContainer = document.getElementById('display-posts');

postsContainer.addEventListener('click', function(e) {
  if (e.target.closest('.like-icon')) {
    const icon = e.target.closest('.like-icon');
    icon.classList.toggle('text-red-500');
  }
  
  if (e.target.closest('.dislike-icon')) {
    const icon = e.target.closest('.dislike-icon');
    icon.classList.toggle('text-blue-500');
  }
  if (e.target.closest('.post-dropdown')){
    const dropdown=e.target.closest('.post-dropdown');
    const menu=dropdown.nextElementSibling;
    menu.classList.toggle('hidden');
    document.addEventListener('click', function(event) {
      if (!dropdown.contains(event.target) && !menu.contains(event.target)) {
        menu.classList.add('hidden');
      }
    });
  }
  if(e.target.closest('delete-icon') || e.target.closest('.delete-icon')){
    const deleteIcon=e.target.closest('.delete-icon');
    const postToDelete=deleteIcon.closest('.post');
    postToDelete.remove();
  }
});

// dropdown menu functionality
const dropdowns=document.getElementById('profile-image')
dropdowns.addEventListener('click',function(e){
  const menu=document.getElementById('dropdownDelay');
  menu.classList.toggle('hidden');
  document.addEventListener('click', function(event) {
    if (!dropdowns.contains(event.target) && !menu.contains(event.target)) {
      menu.classList.add('hidden');
    }
  });
});

