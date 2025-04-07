document.addEventListener("DOMContentLoaded", () => {
  console.log("🌳 The Omniversal Tree has sprouted.");

  const links = document.querySelectorAll("ul li a");
  links.forEach(link => {
    link.addEventListener("mouseover", () => {
      link.style.color = "#0ff"; // highlight on hover
    });

    link.addEventListener("mouseout", () => {
      link.style.color = ""; // revert style
    });
  });

  // Optional: Clicking branches zooms into different areas of map (future feature)
  const map = document.querySelector("#map-container img");
  map.addEventListener("click", (e) => {
    const x = e.offsetX;
    const y = e.offsetY;
    console.log(`🧭 Map clicked at coordinates: (${x}, ${y})`);

    // Future: Detect regions via coordinates or embed SVG map regions
    alert("Coming soon: Interactive navigation between branches!");
  });
});
