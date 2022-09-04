let filterDivs = document.getElementsByClassName('filter-item');

for (let i = 0; i < filterDivs.length; i++) {
    filterDivs[i].addEventListener("click", function () {
        let checkbox = this.getElementsByTagName('input')[0];
        checkbox.checked = !checkbox.checked;
        if (checkbox.checked) {
            this.classList.add('bg-slate-50');
            this.classList.remove('bg-[#ffc6c7]');
        } else {
            this.classList.remove('bg-slate-50');
            this.classList.add('bg-[#ffc6c7]');
        }
    });
}


let navToggle = document.getElementsByClassName('nav-toggle');
let navMenu = document.getElementsByClassName('nav-menu');

navToggle[0].addEventListener("click", function () {
    navMenu[0].classList.toggle('hidden');
    navMenu[0].classList.toggle('flex');
}
);

let filterButton = document.getElementsByClassName('filter-toggle');
let filterMenu = document.getElementsByClassName('filter-menu');

filterButton[0].addEventListener("click", function () {
    filterMenu[0].classList.toggle('hidden');
    filterMenu[0].classList.toggle('flex');
}
);





