import azure.functions as func
import google.generativeai as genai
import os

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="analyze", methods=["POST"])
def analyze(req: func.HttpRequest) -> func.HttpResponse:
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash-001")
    
    try:
        file = req.files.get('file')
        response = model.generate_content(["Analizuj pupila: Fakty, Sens, Zachowanie Bytu.", file.read()])
        return func.HttpResponse(response.text, status_code=200, headers={"Access-Control-Allow-Origin": "*"})
    except Exception as e:
        return func.HttpResponse(f"Błąd: {str(e)}", status_code=500)
