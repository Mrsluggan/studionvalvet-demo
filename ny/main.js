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

