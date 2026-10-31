// Shared presentation runs for server-rendered facts and the daily home hook.
export function figureRuns(text, highlight = false) {
  const unit = /([%％]|\s?(?:(?:兆|億|千萬|百萬|萬|仟|千|百)?(?:美元|美金|港元|日圓|日元|歐元|元)|[兆億萬仟千]))$/;
  const parts = String(text ?? '').split(/([+−-]?\d+(?:[,.]\d+)*(?:[%％]|\s?(?:(?:兆|億|千萬|百萬|萬|仟|千|百)?(?:美元|美金|港元|日圓|日元|歐元|元)|[兆億萬仟千]))?)/g);
  const percent = parts.findIndex((part, i) => i % 2 === 1 && /[%％]$/.test(part));
  const amount = parts.findIndex((part, i) => i % 2 === 1 && (
    /(?:元|圓|美金)$/.test(part) || (/[兆億萬仟千]$/.test(part) && /(?:營收|收入|收益|費用|支出|資本額|金額|餘額)[^。！？；]*$/.test(parts[i - 1]))
  ));
  // One verified percentage or monetary amount; years and counts stay plain.
  const key = highlight ? (percent >= 0 ? percent : amount) : -1;
  return parts.map((text, i) => ({ text, number: i % 2 === 1, key: i === key, runs: text.split(unit) }))
    .filter(({ text }) => text);
}
