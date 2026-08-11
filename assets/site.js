/* Small, dependency-free enhancements. The site works fully without this file. */
(function () {
  "use strict";

  /* Exam countdown: [data-exam-date] holds an ISO date; the baked-in text
     stays as the fallback when JS never runs. */
  document.querySelectorAll("[data-exam-date]").forEach(function (el) {
    var exam = new Date(el.getAttribute("data-exam-date") + "T00:00:00");
    var today = new Date();
    today.setHours(0, 0, 0, 0);
    var days = Math.round((exam - today) / 86400000);
    var out;
    if (days > 1) out = "Exam in " + days + " days";
    else if (days === 1) out = "Exam tomorrow";
    else if (days === 0) out = "Exam today";
    else return;
    el.textContent = out;
  });

  /* Success criteria checkboxes persist per lesson, on this device only. */
  var article = document.querySelector("[data-lesson-key]");
  if (!article) return;
  var key = "y11-2027-crit-" + article.getAttribute("data-lesson-key");
  var boxes = article.querySelectorAll(".crit-list input[type=checkbox]");
  if (!boxes.length) return;

  var saved = {};
  try {
    saved = JSON.parse(window.localStorage.getItem(key) || "{}");
  } catch (err) {
    saved = {};
  }

  boxes.forEach(function (box, i) {
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
