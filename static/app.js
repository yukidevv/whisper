(async () =>{
    const form = document.getElementById("transcribe-form");
    console.log(form);
    const result = document.getElementById("result");

    form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const url = document.getElementById("url").value;
    const model = document.getElementById("model-select").value;

    result.value = "文字起こし中...しばらくお待ちください。";

    const response = await fetch("/api/v1/transcribe", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url, model})
    });
    const data = await response.json();
    result.value = data.text || "エラーが発生しました。";
    });
})();