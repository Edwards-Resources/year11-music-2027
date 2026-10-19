/* Small, dependency-free enhancements. The site works fully without this file:
   the rail simply starts at week 1, and a tick lasts the visit rather than the
   term. Nothing here is load-bearing, and nothing here is a dependency. */
(function () {
  "use strict";

  /* On a phone the rail is a capped scroller. Starting it at week 1 while the
     class is at lesson 9 hides both the lesson being read and the on-air row,
     which is the one thing the rail exists to show. Bring the page's own row
     into view, falling back to the on-air row on the term hub and the home
     page, where no row is being read. */
  var list = document.querySelector(".rlist");
  if (list) {
    var target = list.querySelector('.rl[aria-current="page"]') || list.querySelector(".rl.on");
    if (target && list.scrollHeight > list.clientHeight + 4) {
      var row = target.parentElement || target;
      var top = row.offsetTop - (list.clientHeight - row.offsetHeight) / 2;
      list.scrollTop = Math.max(0, top);
    }
  }

  /* Success criteria ticks persist per lesson, on this device only. Keyed on
     the page path, so a lesson keeps its own ticks and nothing is shared. */
  var boxes = document.querySelectorAll(".crit input[type=checkbox]");
  if (!boxes.length) return;
  var key = "y11-2027-crit:" + window.location.pathname;

  var saved = {};
  try {
    saved = JSON.parse(window.localStorage.getItem(key) || "{}");
  } catch (err) {
    saved = {};
  }

  Array.prototype.forEach.call(boxes, function (box, i) {
    if (saved[i]) box.checked = true;
    box.addEventListener("change", function () {
      saved[i] = box.checked;
      try {
        window.localStorage.setItem(key, JSON.stringify(saved));
      } catch (err) {
        /* Private browsing or a full quota: the tick still works this visit. */
      }
    });
  });
})();
