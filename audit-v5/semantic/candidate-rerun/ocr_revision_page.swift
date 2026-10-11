import Foundation
import Vision
import ImageIO

let imageURL = URL(fileURLWithPath: CommandLine.arguments[1])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[2])
let request = VNRecognizeTextRequest()
request.recognitionLevel = .accurate
request.recognitionLanguages = ["zh-Hant", "en-US"]
request.usesLanguageCorrection = false
let handler = VNImageRequestHandler(url: imageURL, options: [:])
try handler.perform([request])
let observations = (request.results ?? []).compactMap { result -> [String: Any]? in
    guard let candidate = result.topCandidates(1).first else { return nil }
    return ["text": candidate.string, "confidence": candidate.confidence,
            "bounds": [result.boundingBox.origin.x, result.boundingBox.origin.y,
                       result.boundingBox.width, result.boundingBox.height]]
}
let data = try JSONSerialization.data(withJSONObject: observations, options: [.prettyPrinted, .sortedKeys])
try data.write(to: outputURL)
