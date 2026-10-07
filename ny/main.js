// tonar in innehåll när det scrollas fram
const io = new IntersectionObserver(entries => {
  entries.filter(e => e.isIntersecting).forEach(e => {
    e.target.classList.add("in");
    io.unobserve(e.target);
  });
}, {threshold: 0.12});
document.querySelectorAll(".rise").forEach(el => io.observe(el));

// menyn blir vit när den ligger över en bild eller film
const nav = document.querySelector(".nav");
const tone = () => {
  const under = document.elementsFromPoint(40, 34).find(el => !nav.contains(el) && !el.closest(".mark"));
  document.body.classList.toggle("dark", !!(under && under.closest(".full, footer")));
};
addEventListener("scroll", tone, {passive: true});
addEventListener("resize", tone);
tone();

// ljus eller svart/orange – valet sparas mellan sidorna
document.querySelectorAll(".theme button").forEach(b => {
  const sync = () => b.setAttribute("aria-pressed", (document.documentElement.dataset.theme || "light") === b.dataset.t);
  sync();
  b.addEventListener("click", () => {
    document.documentElement.dataset.theme = b.dataset.t;
    try { localStorage.setItem("tema", b.dataset.t); } catch (e) {}
    document.querySelectorAll(".theme button").forEach(x => x.setAttribute("aria-pressed", x === b));
  });
});
