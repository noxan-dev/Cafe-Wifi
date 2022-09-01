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
    }
    );
}


