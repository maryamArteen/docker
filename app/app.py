import time
import redis
from flask import Flask, render_template
import os 
from dotenv import load_dotenv
import pandas as pd
import matplotlib.figure as figure
import io
import base64
from matplotlib.figure import Figure

load_dotenv()

redis_host = os.getenv('REDIS_HOST') or "localhost"
redis_pass = os.getenv('REDIS_PASSWORD') or None

cache = redis.Redis(
    host=redis_host,
    port=6379,
    password=redis_pass
)
app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
@app.route('/')
def hello():
    count = get_hit_count()
    return render_template('hello.html', name= "BIPM", count = count)

# @app.route('/titanic')
# def titanic():
    
# # 1) Load the data and build the table
#     file_path = os.path.join(os.path.dirname(__file__), 'titanic.csv')
#     df = pd.read_csv(file_path)
#     table = df.head().to_html(classes='titanic-table', border=0, index=False)

#     # 2) Compute survivors by gender
#     survivors = df[df['survived'] == 1]['sex'].value_counts()
#     labels = list(survivors.index)
#     values = list(survivors.values)

#     # 3) Build the Matplotlib figure
#     fig = Figure(figsize=(6,4))
#     ax = fig.add_subplot(1,1,1)
#     ax.bar(labels, values, color=['#5dade2', '#f5b7b1'])
#     ax.set_title('Survivors by Gender')
#     ax.set_ylabel('Count')

#     # 4) Serialize it to PNG in-memory
#     buf = io.BytesIO()
#     fig.tight_layout()
#     fig.savefig(buf, format="png")
#     buf.seek(0)
#     plot_data = base64.b64encode(buf.read()).decode('ascii')
#     plot_url = f"data:image/png;base64,{plot_data}"

#     # 5) Render the Titanic template (not hello.html)
#     return render_template(
#         "titanic.html",
#         table=table,
#         plot_url=plot_url,
#         labels=labels,
#         values=values
#     )

# Removed misplaced return statement


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
