// 公司敘述的原始文件；公開說明書的申報月份不當成年報年度。
export const reportName = (report) => report.kind === 'prospectus' ? '公開說明書' : '年報';

export function reportLabel(report) {
  if (report.kind === 'prospectus') {
    const [year, month] = report.filed_month.split('-');
    return `公開說明書（${year} 年 ${Number(month)} 月，${report.doc_label}）`;
  }
  return `${report.fy} 年度年報`;
}
