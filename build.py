from pathlib import Path
import zipfile, shutil
root=Path(__file__).resolve().parent
out=root/'dist'
if out.exists(): shutil.rmtree(out)
out.mkdir()
with zipfile.ZipFile(root/'TIK_VI_Aktivitete.zip') as z:
    for item in z.infolist():
        target=(out/item.filename).resolve()
        if out.resolve() not in target.parents: raise ValueError('Path outside dist')
        if item.is_dir(): continue
        first=Path(item.filename).parts[0]
        if first.startswith('K') or first in ['index.html','style.css','logic.js','app.js','README.md','QA.md']:
            target.parent.mkdir(parents=True,exist_ok=True)
            target.write_bytes(z.read(item))
print('TIK_VI: dist gati për publikim.')
