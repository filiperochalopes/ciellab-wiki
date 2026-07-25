function initializeVideoFallbacks(root = document) {
  root.querySelectorAll(".ciellab-video-wrapper").forEach((wrapper) => {
    if (wrapper.dataset.fallbackInitialized === "true") return;
    wrapper.dataset.fallbackInitialized = "true";

    const video = wrapper.querySelector("video");
    const message = wrapper.querySelector(".ciellab-video-error");
    if (!video || !message || wrapper.classList.contains("ciellab-video-unconfigured")) {
      return;
    }

    const showError = () => {
      video.hidden = true;
      message.hidden = false;
    };

    video.addEventListener("error", showError);
    video.querySelectorAll("source").forEach((source) => {
      source.addEventListener("error", showError);
    });

    if (video.error || video.networkState === HTMLMediaElement.NETWORK_NO_SOURCE) {
      showError();
    }
  });
}

document$.subscribe(() => {
  initializeVideoFallbacks();
});
