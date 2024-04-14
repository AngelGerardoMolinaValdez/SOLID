from report.creator import ReportCreatorJson, ReportCreatorCsv, ReportCreatorXml
from report.viewer import ReportViewerConsole, ReportViewerHtml, ReportViewerJson

def main() -> None:
    data = {"key": "value"}
    report_creator_json = ReportCreatorJson()
    report_creator_csv = ReportCreatorCsv()
    report_creator_xml = ReportCreatorXml()

    report_viewer_console = ReportViewerConsole()
    report_viewer_html = ReportViewerHtml()
    report_viewer_json = ReportViewerJson()

    report_json = report_creator_json.create(data)
    report_csv = report_creator_csv.create(data)
    report_xml = report_creator_xml.create(data)
    print(report_json)
    print(report_csv)
    print(report_xml)

    report_console = report_viewer_console.view(data)
    report_html = report_viewer_html.view(data)
    report_json = report_viewer_json.view(data)
    print(report_console)
    print(report_html)
    print(report_json)

if __name__ == "__main__":
    main()
