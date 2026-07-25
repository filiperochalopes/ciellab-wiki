import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";

mermaid.initialize({
  startOnLoad: false,
  securityLevel: "strict",
  theme: document.body.getAttribute("data-md-color-scheme") === "slate" ? "dark" : "default",
});

document$.subscribe(() => {
  mermaid.run({ querySelector: ".mermaid" });
});

