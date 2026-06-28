# plugin-ftp

Aurora connector plugin — **FTP / FTPS**.

A standalone Aurora package containing the `ftp` connector (built on `ftplib`,
no extra dependencies).

## Operations
`upload` · `download` · `listFiles` · `delete`

## Install (Aurora engine)
Add a **Git Source** pointing at this repo:
- URL: `https://github.com/AURORA-INTEGRATION/plugin-ftp`
- Branch: `main`
- Packages subfolder: `packages` (default)

The engine loads `packages/ftp/`, registers connector type `ftp` and its
operation services (`common.connectors.ftp.*`). Create a connector instance
under **Connectors** (host / port / username / password / secure / passive),
then drop an `ftp` operation into a flow.

## Layout
```
packages/ftp/
  package.yml
  connectors/ftp/
    connector.yml
    client.py          # ftplib connect / upload / download / list / delete
    operations/<op>/   # python_service (.yml + .py) with a ui: block
```
