import random

import pieces
import rules
from mechanics import *


class Bot(object):
    def __init__(self, player):
        self.player = player

    def doTurn(self, board, fails=0):
        raise NotImplementedError

    def pieceValue(self, piece):
        if pieces.isPawn(piece):   return 1
        if pieces.isKnight(piece): return 3
        if pieces.isBishop(piece): return 3
        if pieces.isRook(piece):   return 5
        if pieces.isQueen(piece):  return 9
        if pieces.isKing(piece):
            return 5
        else:
            return 0

    def scoreHeuristic(self, board):
        playerPieces = [piece for piece, x, y in allPieces(board, player=self.player)]
        notPlayerPieces = [piece for piece, x, y in allPieces(board, player=pieces.notPlayer(self.player))]
        playerValue = sum([self.pieceValue(piece) for piece in playerPieces])
        notPlayerValue = sum([self.pieceValue(piece) for piece in notPlayerPieces])
        score = playerValue - notPlayerValue
        return score


class RandoBot(Bot):
    """ A bot that makes completely random moves """

    def doTurn(self, board, fails=0):
        myPieces = allPieces(board, player=self.player)
        while True:
            piece, pieceX, pieceY = random.choice(myPieces)
            possiblePiecesMoves = rules.possibleMoves(board, pieceX, pieceY)
            if possiblePiecesMoves:
                moveX, moveY = random.choice(possiblePiecesMoves)
                return (piece, pieceX, pieceY, moveX, moveY)


class OneDepthBot(Bot):
    """ 
    A bot that makes moves with the highest scoreHeuristic, based on a depth search of 1
    """

    def doTurn(self, board, fails=0):
        movedBoardScores = []  # A list of (score, (piece, pieceX, pieceY, moveX, moveY))
        myPieces = allPieces(board, player=self.player)
        for piece, pieceX, pieceY in myPieces:
            possiblePiecesMoves = rules.possibleMoves(board, pieceX, pieceY)
            for moveX, moveY in possiblePiecesMoves:
                movedBoard = movePiece(board, piece, pieceX, pieceY, moveX, moveY)
                movedBoardScore = self.scoreHeuristic(movedBoard)
                movedBoardScores.append((movedBoardScore, (piece, pieceX, pieceY, moveX, moveY)))
        movedBoardScores.sort()
        fails_offset = -1 + fails
        _, winningMove = movedBoardScores[fails_offset]
        return winningMove


class DepthBot(Bot):
    """
    Minimax bot
    """

    def doTurn(self, board, fails=-1):
        movedBoardScores = []  # A list of (score, (piece, pieceX, pieceY, moveX, moveY))

        myPieces = allPieces(board, player=self.player)
        for piece, pieceX, pieceY in myPieces:
            possiblePiecesMoves = rules.possibleMoves(board, pieceX, pieceY)
            for moveX, moveY in possiblePiecesMoves:
                movedBoard = movePiece(board, piece, pieceX, pieceY, moveX, moveY)
                score = self.miniMax(movedBoard, self.player)
                movedBoardScores.append((score, (piece, pieceX, pieceY, moveX, moveY)))

        movedBoardScores.sort(reverse=True)

        if fails >= 0:
            index = fails
        else:
            index = min(len(movedBoardScores) - 1, max(1, round(random.expovariate(0.5))))

        _, winningMove = movedBoardScores[index]
        return winningMove

    def miniMax(self, board, currentPlayer, depth=2):
        if depth == 0:
            return 0

        myPieces = allPieces(board, player=currentPlayer)

        if not myPieces:
            return 0

        results = []
        score = self.scoreHeuristic(board)
        for piece, pieceX, pieceY in myPieces:
            possiblePiecesMoves = rules.possibleMoves(board, pieceX, pieceY)
            for moveX, moveY in possiblePiecesMoves:
                movedBoard = movePiece(board, piece, pieceX, pieceY, moveX, moveY)
                result = self.miniMax(movedBoard, pieces.notPlayer(currentPlayer), depth - 1)
                result += score
                results.append(result)

        # Case where list is empty
        results.append(0)

        return max(results)
