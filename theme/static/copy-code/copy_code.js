let codes = document.querySelectorAll('div.highlight pre code');
let countID = 0;
codes.forEach((code) => {

  code.setAttribute("id", "code" + countID);

  let btn = document.createElement('button');
  btn.innerHTML = '<i class="fas fa-copy" aria-hidden="true"></i><span class="tooltiptext">Copy Code</span>';
  btn.className = "btn-copy";
  btn.setAttribute("data-clipboard-action", "copy");
  btn.setAttribute("data-clipboard-target", "#code" + countID);

  code.parentNode.before(btn);
  //code.parentNode.parentNode.parentNode.parentNode.parentNode.parentNode.before(btn);

  countID++;
});

let clipboard = new ClipboardJS('.btn-copy');
