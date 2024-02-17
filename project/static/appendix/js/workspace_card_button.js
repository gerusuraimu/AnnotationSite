function setMethod(Id) {
    let form = document.getElementById('workspace-btn-' + Id);
    let work = document.getElementById('workspace-name-' + Id);
    let spc = document.getElementById('space-name-' + Id);
    let rnm = document.getElementById('rename-btn-' + Id);
    let dlt = document.getElementById('delete-btn-' + Id);

    rnm.addEventListener('click', () => {
        if (rnm.classList.contains('btn-outline-success')) {
            spc.classList.add('edit');
            spc.disabled = false;
            spc.focus();
            rnm.classList.remove('btn-outline-success');
            rnm.classList.add('btn-success');
        } else if (rnm.classList.contains('btn-success')) {
            spc.classList.remove('edit');
            spc.disabled = true;
            work.value = spc.value;
            rnm.classList.remove('btn-success');
            rnm.classList.add('btn-outline-success');
            form.action = '/workspace/rename';
            form.submit();
        }
    });

    dlt.addEventListener('click', () => {
        form.action = '/workspace/delete';
        form.submit();
    });
}