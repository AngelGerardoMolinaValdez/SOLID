from issues.call import IssueCall
from issues.log import IssueLoggerPdf, IssueLoggerHtml, IssueLoggerPlainText

def main():
    issue_pdf = IssueLoggerPdf()
    issue_error = IssueCall('ERROR')
    print(issue_pdf.log(issue_error.process()))

    issue_html = IssueLoggerHtml()
    issue_process = IssueCall('PROCESS')
    print(issue_html.log(issue_process.process()))

    issue_plain_text = IssueLoggerPlainText()
    issue_task = IssueCall('TASK')
    print(issue_plain_text.log(issue_task.process()))

if __name__ == "__main__":
    main()
