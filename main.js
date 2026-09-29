// låt bollarna poppa fram när de syns, en i taget
const io = new IntersectionObserver(entries => {
  entries.filter(e => e.isIntersecting).forEach((e, i) => {
    e.target.style.setProperty("--d", i * 0.12 + "s");
    e.target.classList.add("in");
    io.unobserve(e.target);
  });
}, {threshold: 0.15});
document.querySelectorAll(".pop").forEach(el => io.observe(el));
