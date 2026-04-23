function showmenu(){
    var btn = document.getElementById("butto_menu")
    var nav = document.getElementsByName("main-menu")

    if (nav[0].classList.contains("active")){
        btn.innerText = "X"
    }else{
        btn.innerText = "≡"
    }

    nav[0].classList.toggle("active")
}

const filterBtns = document.querySelectorAll('.filter_btn');
        const galleryItems = document.querySelectorAll('.gallery_item');

        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Toggle active class on buttons
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filter = btn.dataset.filter;

                galleryItems.forEach(item => {
                    // Show all items when "all" is selected, otherwise match category
                    const match = filter === 'all' || item.dataset.category === filter;
                    item.style.display = match ? 'block' : 'none';
                });
            });
        });