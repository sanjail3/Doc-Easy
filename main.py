from openai import OpenAI
import streamlit as st
from streamlit_ace import st_ace

api_key = st.secrets["OPENAI_API_KEY"]
openai_cli = OpenAI(api_key=api_key)

def check_if_not_null(query):
    if query == "":
        return 0
    else:
        return 1

def prompt_to_write_doc(prompt, language):
    agent = f'''you are professional  comments writer for the code I will provide 
    you the code your job is write a well defined comments and doc string for the code I provide in this language {language} 
    give me only the return code with comments and doc strings other than that don't return anything  don't make error in the code only add comments and doc string 
    ```javascript'``` don 't put like this   or name of language in output
'''

    response = openai_cli.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": agent},
                  {"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def app():
    st.set_page_config(page_icon="💻", layout="wide")

    st.write(
        "<div style='text-align: center'><h1>Doc <em style='text-align: center; color: #238636;'>Easy</em></h1></div>",
        unsafe_allow_html=True)

    LANGUAGES = [
        "abap", "abc", "actionscript", "ada", "alda", "apache_conf", "apex", "applescript", "aql",
        "asciidoc", "asl", "assembly_x86", "autohotkey", "batchfile", "c9search", "c_cpp", "cirru",
        "clojure", "cobol", "coffee", "coldfusion", "crystal", "csharp", "csound_document", "csound_orchestra",
        "csound_score", "csp", "css", "curly", "d", "dart", "diff", "django", "dockerfile", "dot", "drools",
        "edifact", "eiffel", "ejs", "elixir", "elm", "erlang", "forth", "fortran", "fsharp", "fsl", "ftl",
        "gcode", "gherkin", "gitignore", "glsl", "gobstones", "golang", "graphqlschema", "groovy", "haml",
        "handlebars", "haskell", "haskell_cabal", "haxe", "hjson", "html", "html_elixir", "html_ruby", "ini",
        "io", "jack", "jade", "java", "javascript", "json", "json5", "jsoniq", "jsp", "jssm", "jsx", "julia",
        "kotlin", "latex", "less", "liquid", "lisp", "livescript", "logiql", "logtalk", "lsl", "lua", "luapage",
        "lucene", "makefile", "markdown", "mask", "matlab", "maze", "mediawiki", "mel", "mixal", "mushcode",
        "mysql", "nginx", "nim", "nix", "nsis", "nunjucks", "objectivec", "ocaml", "pascal", "perl", "perl6",
        "pgsql", "php", "php_laravel_blade", "pig", "plain_text", "powershell", "praat", "prisma", "prolog",
        "properties", "protobuf", "puppet", "python", "qml", "r", "razor", "rdoc", "red", "redshift", "rhtml",
        "rst", "ruby", "rust", "sass", "scad", "scala", "scheme", "scss", "sh", "sjs", "slim", "smarty",
        "snippets", "soy_template", "space", "sparql", "sql", "sqlserver", "stylus", "svg", "swift", "tcl",
        "terraform", "tex", "text", "textile", "toml", "tsx", "turtle", "twig", "typescript", "vala", "vbscript",
        "velocity", "verilog", "vhdl", "visualforce", "wollok", "xml", "xquery", "yaml"
    ]

    THEMES = [
        "ambiance", "chaos", "chrome", "clouds", "clouds_midnight", "cobalt", "crimson_editor", "dawn",
        "dracula", "dreamweaver", "eclipse", "github", "gob", "gruvbox", "idle_fingers", "iplastic",
        "katzenmilch", "kr_theme", "kuroir", "merbivore", "merbivore_soft", "mono_industrial", "monokai",
        "nord_dark", "pastel_on_dark", "solarized_dark", "solarized_light", "sqlserver", "terminal",
        "textmate", "tomorrow", "tomorrow_night", "tomorrow_night_blue", "tomorrow_night_bright",
        "tomorrow_night_eighties", "twilight", "vibrant_ink", "xcode"
    ]

    inp_language = st.sidebar.selectbox('Select Input Language', LANGUAGES, index=121)

    st.markdown("## Input:")
    user_input = st_ace(
        value="",
        placeholder="Write your code or prompt here ...",
        height=600,
        language=inp_language,
        theme=st.sidebar.selectbox('Select Editor Theme', THEMES, index=5)
    )

    st.markdown("## Output:")

    fix_doc_button = st.sidebar.button('Doc Writer')

    if fix_doc_button:
        st.write('Button clicked!')
        answer = prompt_to_write_doc(user_input, inp_language)
        st_ace(value=answer,height=600,
        language=inp_language,theme="cobalt")
        # st.code(answer, language='text')




def main():
    app()

if __name__ == "__main__":
    main()

